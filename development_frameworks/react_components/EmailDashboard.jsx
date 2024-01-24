import React, { useState, useEffect } from 'react';
import { trackEmail, userPreferences, systemSettings } from '../../shared_dependencies';
import './email_dashboard.css';

const EmailDashboard = () => {
  const [emails, setEmails] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Fetch emails from Outlook integration
    const fetchEmails = async () => {
      try {
        const response = await fetch('/api/email', {
          headers: {
            'Authorization': `Bearer ${systemSettings.apiKeys.outlook}`,
            'Content-Type': 'application/json'
          }
        });
        if (!response.ok) {
          throw new Error('Error fetching emails');
        }
        const data = await response.json();
        setEmails(data);
      } catch (error) {
        console.error('Failed to fetch emails:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchEmails();
  }, []);

  const handleEmailClick = (emailId) => {
    // Placeholder for email click handling logic
    trackEmail(emailId);
  };

  return (
    <div id="email-dashboard-container" className="email-dashboard">
      <h1>Email Management</h1>
      {loading ? (
        <p>Loading emails...</p>
      ) : (
        <ul className="email-list">
          {emails.map((email) => (
            <li key={email.id} className="email-item" onClick={() => handleEmailClick(email.id)}>
              <div className="email-sender">{email.sender}</div>
              <div className="email-subject">{email.subject}</div>
              <div className="email-preview">{email.preview}</div>
              <div className="email-date">{new Date(email.date).toLocaleString()}</div>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default EmailDashboard;