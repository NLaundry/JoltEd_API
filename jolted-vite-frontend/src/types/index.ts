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

export interface WikiModuleData {
    topic: string,
    identity?: string,
    target_audience?: string,
    model?: string,
}
