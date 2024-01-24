import React, { useState, useEffect } from 'react';
import { fetchSocialMediaData } from '../../api_integration/social_media_api';
import { fetchEmailData } from '../../api_integration/email_api';
import { fetchContentData } from '../../api_integration/content_api';
import { fetchDesignData } from '../../api_integration/design_api';
import SocialMediaDashboard from './SocialMediaDashboard';
import EmailDashboard from './EmailDashboard';
import ContentCalendar from './ContentCalendar';
import DesignInterface from './DesignInterface';
import ChatWindow from './ChatWindow';
import '../ui_elements/ui_styles.css';
import './Dashboard.css';

const Dashboard = () => {
  const [socialMediaData, setSocialMediaData] = useState(null);
  const [emailData, setEmailData] = useState(null);
  const [contentData, setContentData] = useState(null);
  const [designData, setDesignData] = useState(null);

  useEffect(() => {
    async function loadData() {
      try {
        const socialData = await fetchSocialMediaData();
        const emailInfo = await fetchEmailData();
        const contentInfo = await fetchContentData();
        const designInfo = await fetchDesignData();
        setSocialMediaData(socialData);
        setEmailData(emailInfo);
        setContentData(contentInfo);
        setDesignData(designInfo);
      } catch (error) {
        console.error('Error loading dashboard data:', error);
      }
    }
    loadData();
  }, []);

  return (
    <div className="dashboard-container" id="dashboard-container">
      <SocialMediaDashboard data={socialMediaData} />
      <EmailDashboard data={emailData} />
      <ContentCalendar data={contentData} />
      <DesignInterface data={designData} />
      <ChatWindow />
    </div>
  );
};

export default Dashboard;