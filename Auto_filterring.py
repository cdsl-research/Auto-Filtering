from flask import Flask, request, jsonify
import slackweb
from monitoring_weight import weight_calculation
app = Flask(__name__)


# Example usage:
result = weight_calculation()
print(result)

# Slackに通知する関数
def notification(message):
    slack = slackweb.Slack("https://hooks.slack.com/services/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")
    slack.notify(text=str(message))

# アラートメッセージをフォーマットする関数
def format_alert_message(alert):
    status = alert.get('status')
    labels = alert.get('labels', {})
    annotations = alert.get('annotations', {})
    startsAt = alert.get('startsAt')
    endsAt = alert.get('endsAt')
    generatorURL = alert.get('generatorURL')

    alert_message = (
        f"Status: {status}\n"
        f"Alert Name: {labels.get('alertname')}\n"
        f"Instance: {labels.get('instance')}\n"
        f"Severity: {labels.get('severity')}\n"
        f"Starts At: {startsAt}\n"
        f"Ends At: {endsAt}\n"
        f"Generator URL: {generatorURL}\n"
        f"Labels: {labels}\n"
        f"Annotations: {annotations}\n"
    )
    return alert_message

# /alert ルートのPOSTリクエストを処理する
@app.route('/alert', methods=['POST'])
def alert():
    data = request.json
    alerts = data.get('alerts', [])
    
    for alert in alerts:
        instance = alert.get('labels', {}).get('instance', '')

        # Example usage:
        result = weight_calculation()
        print(result)

        if instance in "outside-nfs3:9100":
        # instanceが重要なインスタンスに含まれている場合に通知を行う
            formatted_alert = format_alert_message(alert)
            notification(formatted_alert)
    
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
