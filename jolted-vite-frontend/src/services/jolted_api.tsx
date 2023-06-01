import axios from 'axios';

export interface ModuleData {
    topic: string,
    identity?: string,
    target_audience?: string,
    model?: string,
}

const apiClient = axios.create({
  baseURL: 'http://localhost:8000',
});

export const createNotebookModule = async (data: ModuleData) => {
  try {
    const response = await apiClient.post('/create_notebook_module', data);
    return response.data;
  } catch (error) {
    console.error('Error creating notebook module:', error);
    throw error;
  }
};

export const createWikiModule = async (data: ModuleData) => {
  try {
    const response = await apiClient.post('/create_wiki_module', data);
    return response.data;
  } catch (error) {
    console.error('Error creating wiki module:', error);
    throw error;
  }
};
