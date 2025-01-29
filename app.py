from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
import re

app = Flask(__name__)

# Flask-Mail Configuration (Use SMTP for sending emails)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # For Gmail, or adjust if using another provider
app.config['MAIL_PORT'] = 587  # Use 465 for SSL, 587 for TLS
app.config['MAIL_USE_TLS'] = True  # Use TLS
app.config['MAIL_USERNAME'] = 'your-email@gmail.com'  # Your Gmail address
app.config['MAIL_PASSWORD'] = 'your-email-password'  # Your email password (or app-specific password)
app.config['MAIL_DEFAULT_SENDER'] = 'your-email@gmail.com'

mail = Mail(app)

# Secret key to allow flashing messages
app.secret_key = 'your-secret-key'

@app.route('/', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        # Validate the form inputs
        if not name or not email or not subject or not message:
            flash('All fields are required!', 'error')
            return redirect(url_for('contact'))

        # Email validation
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            flash('Invalid email address!', 'error')
            return redirect(url_for('contact'))

        # Compose email message
        msg = Message(subject,
                      recipients=['recipient@example.com'],  # Replace with the real recipient's email
                      body=f"Message from: {name}\nEmail: {email}\n\n{message}")

        try:
            # Send the email
            mail.send(msg)
            flash('Your message has been sent successfully!', 'success')
            return redirect(url_for('contact'))
        except Exception as e:
            flash(f'Error: {str(e)}', 'error')
            return redirect(url_for('contact'))

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
