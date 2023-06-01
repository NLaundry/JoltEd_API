import Editor from './components/Editor';
import { createNotebookModule, createWikiModule, ModuleData } from './services/jolted_api';
import './App.css'

async function createModule() {
    const data: ModuleData = {
        topic: 'React',
        identity: 'professor of computer science',
        target_audience: 'first year computer science students',
        model: 'gpt-3.5-turbo',
    };

    try {
        console.log(data)
        const wikiModule = await createWikiModule(data);
        console.log('Created wiki module:', wikiModule);
    } catch (error) {
        console.error('Error creating module:', error);
    }
}

function App() {

    return (
        <div className="container mx-auto">
            <button onClick={createModule}>Create Module</button>
            <Editor />
        </div>
    )
}

export default App
