import React, { useState } from 'react';
import { createDesign } from '../../graphics_design/design_tools';
import './design_interface.css';

const DesignInterface = () => {
  const [designInput, setDesignInput] = useState('');
  const [designs, setDesigns] = useState([]);

  const handleDesignCreation = async () => {
    try {
      const newDesign = await createDesign(designInput);
      setDesigns([...designs, newDesign]);
      setDesignInput('');
    } catch (error) {
      console.error('Error creating design:', error);
    }
  };

  return (
    <div id="design-interface-container" className="design-interface">
      <h2>Graphics Design Interface</h2>
      <textarea
        value={designInput}
        onChange={(e) => setDesignInput(e.target.value)}
        placeholder="Enter design parameters"
        className="design-input"
      />
      <button onClick={handleDesignCreation} className="design-submit-btn">
        Create Design
      </button>
      <div className="designs-gallery">
        {designs.map((design, index) => (
          <div key={index} className="design-item">
            <img src={design.imageUrl} alt={`Design ${index + 1}`} />
          </div>
        ))}
      </div>
    </div>
  );
};

export default DesignInterface;