export interface CurriculumData {
  topics: string[];
  subtopics: string[];
}

export interface NotebookModuleData {
    topic: string,
    identity?: string,
    target_audience?: string,
    model?: string,
}

/**
 * Represents a wiki module.
 * @property {string} id - The unique identifier of the wiki module.
 * @property {string} title - The title of the wiki module.
 * @property {string} content - The content of the wiki module.
 */
export type WikiModule = {
  id: string;
  title: string;
  content: string;
};

/**
 * @property {string} topic - The topic of the wiki module.
 * @property {string} [identity] - The identity of the wiki module.
 * @property {string} [target_audience] - The target audience of the wiki module.
 * @property {string} [model] - The model of the wiki module.
 */
export interface WikiModuleCreate {
    topic: string;
    identity?: string;
    target_audience?: string;
    model?: string;
}
