# Author: Your Name Here

# Developed by <your name>

from flask import Blueprint, request, jsonify
from .models import ExpenseRecord, BudgetPlan, ProfileUser, SharedCircle
from .db_config import db
from datetime import datetime

api = Blueprint('api', __name__)

@api.route('/add_expense', methods=['POST'])
def add_expense_entry():
    data = request.get_json()
    entry = ExpenseRecord(
        tag=data['tag'],
        cost=data['cost'],
        recorded_on=datetime.strptime(data['date'], "%Y-%m-%d")
    )
    db.session.add(entry)
    db.session.commit()
    return jsonify({"message": "Expense added successfully"})

@api.route('/set_budget', methods=['POST'])
def set_budget_plan():
    data = request.get_json()
    plan = BudgetPlan(
        tag=data['tag'],
        month_key=data['month'],
        limit_amount=data['amount']
    )
    db.session.add(plan)
    db.session.commit()
    return jsonify({"message": "Budget set successfully"})

@api.route('/report/<month>', methods=['GET'])
def monthly_report(month):
    expenses = ExpenseRecord.query.filter(
        ExpenseRecord.recorded_on.like(f"{month}-%")
    ).all()
    budgets = BudgetPlan.query.filter_by(month_key=month).all()

    usage = {}
    for exp in expenses:
        usage.setdefault(exp.tag, 0)
        usage[exp.tag] += exp.cost

    summary = []
    for plan in budgets:
        spent = usage.get(plan.tag, 0)
        summary.append({
            "tag": plan.tag,
            "budget": plan.limit_amount,
            "used": spent,
            "status": "Exceeded" if spent > plan.limit_amount else "Within Budget"
        })

    return jsonify(summary)

@api.route('/trigger_alerts/<email>/<month>', methods=['GET'])
def trigger_budget_alerts(email, month):
    user = ProfileUser.query.filter_by(email=email).first()
    if not user:
        return jsonify({"error": "User not found"}), 404

    expenses = ExpenseRecord.query.filter(
        ExpenseRecord.recorded_on.like(f"{month}-%")
    ).all()
    plans = BudgetPlan.query.filter_by(month_key=month).all()

    usage = {}
    alerts = []

    for e in expenses:
        usage.setdefault(e.tag, 0)
        usage[e.tag] += e.cost

    for plan in plans:
        spent = usage.get(plan.tag, 0)
        remain = plan.limit_amount - spent
        if 0 < remain <= 0.1 * plan.limit_amount:
            alerts.append({
                "tag": plan.tag,
                "remaining": remain,
                "notice": "Budget nearing limit!"
            })

    if alerts:
        send_email_simulation(user.email, "Budget Alert", "
".join([a['tag'] for a in alerts]))

    return jsonify(alerts)

def send_email_simulation(to_email, subject, content):
    print(f"[SIMULATED EMAIL] To: {to_email}\nSubject: {subject}\n{content}")

@api.route('/submit_group_expense', methods=['POST'])
def submit_group_expense():
    data = request.get_json()
    group = SharedCircle.query.get(data['circle_id'])
    if not group or not group.users:
        return jsonify({"error": "Group not found"}), 404

    share = data['cost'] / len(group.users)
    for member in group.users:
        record = ExpenseRecord(
            tag=data['tag'],
            cost=share,
            recorded_on=datetime.strptime(data['date'], "%Y-%m-%d")
        )
        db.session.add(record)

    db.session.commit()
    return jsonify({"message": f"Shared expense logged for {len(group.users)} users"})