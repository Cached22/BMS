import React, { useState } from 'react';
import './chat_window.css';
import { sendMessage } from '../../ai_chat_assistant/chat_assistant.py';

const ChatWindow = () => {
  const [message, setMessage] = useState('');
  const [conversation, setConversation] = useState([]);

  const handleInputChange = (event) => {
    setMessage(event.target.value);
  };

  const handleSendMessage = async () => {
    if (message.trim() === '') return;

    const newMessage = {
      text: message,
      sender: 'user',
      timestamp: new Date().toISOString(),
    };

    setConversation([...conversation, newMessage]);

    const botResponse = await sendMessage(message);
    setConversation([...conversation, newMessage, botResponse]);

    setMessage('');
  };

  return (
    <div id="chat-window-container">
      <div className="chat-window">
        <div className="chat-header">
          <h2>AI Assistant</h2>
        </div>
        <div className="chat-body">
          {conversation.map((msg, index) => (
            <div key={index} className={`chat-message ${msg.sender}`}>
              <div className="message-content">{msg.text}</div>
              <div className="message-timestamp">{msg.timestamp}</div>
            </div>
          ))}
        </div>
        <div className="chat-footer">
          <input
            type="text"
            value={message}
            onChange={handleInputChange}
            placeholder="Type your message here..."
            className="chat-input"
          />
          <button onClick={handleSendMessage} className="send-button">
            Send
          </button>
        </div>
      </div>
    </div>
  );
};

export default ChatWindow;