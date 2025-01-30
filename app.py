from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message

app = Flask(__name__)

# Set secret key for flash messages
app.secret_key = 'your_secret_key'

# Set up Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Use Gmail SMTP server (or your email provider)
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email@gmail.com'  # Your email address
app.config['MAIL_PASSWORD'] = 'your_email_password'  # Your email password

mail = Mail(app)

# Route for the contact form
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        # Send email
        msg = Message(subject, sender=email, recipients=['your_email@gmail.com'])
        msg.body = f"Message from: {name}\n\nEmail: {email}\n\nMessage: {message}"
        try:
            mail.send(msg)
            flash(('success', 'Your message has been sent!'))
        except:
            flash(('error', 'There was an error sending your message. Please try again.'))

        return redirect(url_for('contact'))  # Redirect to same page to show success/error message

    return render_template('index.html')  # Change 'index.html' to the name of your template
    
if __name__ == '__main__':
    app.run(debug=True)
