import Editor from './components/Editor';
import WikiModuleCreateForm from './components/WikiModuleCreateForm';
import { createWikiModule } from './services/wikiModuleService.ts'
import { WikiModule, WikiModuleCreate } from './types/index.ts';
import WikiModuleContext from './services/wikiModuleContextService.ts'
import { useState, useEffect } from 'react';
import './App.css'

function App() {

    const [createdWikiModule, setCreatedWikiModule] = useState<WikiModule | null>(null);

    useEffect(() => {
        if (createdWikiModule) {
            console.log('Created wiki module:', createdWikiModule);
        }
    }, [createdWikiModule]);


    return (
        <WikiModuleContext.Provider value={{ createdWikiModule, setCreatedWikiModule }}>
            <div className="container mx-auto">
                <WikiModuleCreateForm />
                <Editor wikiModule={createdWikiModule} />
            </div>
        </WikiModuleContext.Provider>
    )
}

export default App
