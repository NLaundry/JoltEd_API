import { WikiModule, WikiModuleCreate } from "../types/index.ts";


import { createContext } from 'react';


const apiEndpoint = "http://localhost:8000"; // Replace with your API endpoint

/**
 * Creates a new wiki module.
 * @function
 * @async
 * @param {WikiModuleCreate} wikiModule - The wiki module to create.
 * @returns {Promise<WikiModule>} The created wiki module.
 * @throws {Error} If there is a problem with the API request.
 */
export async function createWikiModule(wikiModule: WikiModuleCreate): Promise<WikiModule> {
    const response = await fetch(`${apiEndpoint}/wiki_module/create`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(wikiModule),
    });

    if (!response.ok) {
        throw new Error(`Failed to create wiki module: ${response.statusText}`);
    }

    return response.json();
}


/**
 * Retrieves all wiki modules.
 * @function
 * @async
 * @returns {Promise<WikiModule[]>} A list of all wiki modules.
 * @throws {Error} If there is a problem with the API request.
 */
export async function getAllWikiModules(): Promise<WikiModule[]> {
    const response = await fetch(`${apiEndpoint}/wiki_module/get_all`);

    if (!response.ok) {
        throw new Error(`Failed to get all wiki modules: ${response.statusText}`);
    }

    return response.json();
}

/**
 * Updates the content of a wiki module.
 * @function
 * @async
 * @param {string} wikiModuleId - The ID of the wiki module to update.
 * @param {string} wikiContent - The new content for the wiki module.
 * @returns {Promise<WikiModule>} The updated wiki module.
 * @throws {Error} If there is a problem with the API request.
 */
export async function updateWikiModule(wikiModuleId: string, wikiContent: string): Promise<WikiModule> {
    const response = await fetch(`${apiEndpoint}/wiki_module/update/${wikiModuleId}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ wikiContent }),
    });

    if (!response.ok) {
        throw new Error(`Failed to update wiki module: ${response.statusText}`);
    }

    return response.json();
}

/**
 * Deletes a wiki module by its ID.
 * @function
 * @async
 * @param {string} wikiModuleId - The ID of the wiki module to delete.
 * @returns {Promise<WikiModule>} The deleted wiki module.
 * @throws {Error} If there is a problem with the API request.
 */
export async function deleteWikiModule(wikiModuleId: string): Promise<WikiModule> {
    const response = await fetch(`${apiEndpoint}/wiki_module/delete/${wikiModuleId}`, { method: "DELETE" });

    if (!response.ok) {
        throw new Error(`Failed to delete wiki module: ${response.statusText}`);
    }

    return response.json();
}

/**
 * Retrieves a wiki module by its ID.
 * @function
 * @async
 * @param {string} wikiModuleId - The ID of the wiki module to retrieve.
 * @returns {Promise<WikiModule>} The wiki module.
 * @throws {Error} If there is a problem with the API request.
 */
export async function getWikiModuleById(wikiModuleId: string): Promise<WikiModule> {
    const response = await fetch(`${apiEndpoint}/wiki_module/get_by_id/${wikiModuleId}`);

    if (!response.ok) {
        throw new Error(`Failed to get wiki module by ID: ${response.statusText}`);
    }

    return response.json();
}
