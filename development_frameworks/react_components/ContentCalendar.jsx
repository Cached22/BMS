import React, { useState } from 'react';
import FullCalendar from '@fullcalendar/react';
import dayGridPlugin from '@fullcalendar/daygrid';
import interactionPlugin from '@fullcalendar/interaction';
import { ContentItem } from '../../shared_dependencies';
import '../../ui_elements/ui_styles.css';

const ContentCalendar = () => {
  const [contentItems, setContentItems] = useState([]);

  const handleDateClick = (arg) => {
    // Placeholder for date click logic, potentially to add new content items
    console.log(`Date clicked: ${arg.dateStr}`);
  };

  const handleEventClick = (clickInfo) => {
    // Placeholder for event click logic, potentially to edit or delete content items
    console.log(`Event clicked: ${clickInfo.event.title}`);
  };

  const renderEventContent = (eventInfo) => {
    return (
      <>
        <b>{eventInfo.timeText}</b>
        <i>{eventInfo.event.title}</i>
      </>
    );
  };

  return (
    <div id="content-calendar-container">
      <FullCalendar
        plugins={[dayGridPlugin, interactionPlugin]}
        initialView="dayGridMonth"
        events={contentItems.map(item => ({
          title: item.title,
          start: item.startDate,
          end: item.endDate,
          extendedProps: {
            platform: item.platform
          }
        }))}
        dateClick={handleDateClick}
        eventContent={renderEventContent}
        eventClick={handleEventClick}
      />
    </div>
  );
};

export default ContentCalendar;