// WikiModuleContext.ts
import { createContext } from 'react';
import { WikiModule } from '../types/index.ts';

interface WikiModuleContextType {
  createdWikiModule: WikiModule | null;
  setCreatedWikiModule: (wikiModule: WikiModule) => void;
}

const WikiModuleContext = createContext<WikiModuleContextType>({
  createdWikiModule: null,
  setCreatedWikiModule: (wikiModule: WikiModule) => {},
});

export default WikiModuleContext;
