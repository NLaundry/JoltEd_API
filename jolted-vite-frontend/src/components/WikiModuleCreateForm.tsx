import React, { useState, useContext } from 'react';
import { createWikiModule } from '../services/wikiModuleService.ts'
import { WikiModule, WikiModuleCreate } from '../types/index.ts';
import WikiModuleContext from '../services/wikiModuleContextService.ts'

const WikiModuleCreateForm = () => {
  const [topic, setTopic] = useState('');
  const [identity, setIdentity] = useState('');
  const [targetAudience, setTargetAudience] = useState('');
  const [model, setModel] = useState('');

  // Access the context values
  const { setCreatedWikiModule } = useContext(WikiModuleContext);

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();

    const wikiModule: WikiModuleCreate = {
      topic,
      identity: identity || undefined,
      target_audience: targetAudience || undefined,
      model: model || undefined,
    };
    try {
      const createdWikiModule: WikiModule = await createWikiModule(wikiModule);
      setCreatedWikiModule(createdWikiModule);
      console.log('Created wiki module:', createdWikiModule);
    } catch (error) {
      console.error('Error creating wiki module:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <label htmlFor="topic">Topic:</label>
      <input
        id="topic"
        type="text"
        value={topic}
        onChange={(event) => setTopic(event.target.value)}
      />
      <br />
      <label htmlFor="identity">Identity:</label>
      <input
        id="identity"
        type="text"
        value={identity}
        onChange={(event) => setIdentity(event.target.value)}
      />
      <br />
      <label htmlFor="target_audience">Target Audience:</label>
      <input
        id="target_audience"
        type="text"
        value={targetAudience}
        onChange={(event) => setTargetAudience(event.target.value)}
      />
      <br />
      <label htmlFor="model">Model:</label>
      <input
        id="model"
        type="text"
        value={model}
        onChange={(event) => setModel(event.target.value)}
      />
      <br />
      <button type="submit">Create Wiki Module</button>
    </form>
  );
};

export default WikiModuleCreateForm;
