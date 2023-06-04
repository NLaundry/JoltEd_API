import React from "react";
import { useEffect, useState } from "react";
import { BlockNoteEditor, Block } from "@blocknote/core";
import { BlockNoteView, useBlockNote } from "@blocknote/react";
import { WikiModule } from '../types/index.ts';
import "@blocknote/core/style.css";

const Editor: React.FC<{ wikiModule: WikiModule | null }> = ({ wikiModule }) => {
    // Creates a new editor instance.
    const editor: BlockNoteEditor | null = useBlockNote({});
    console.log(wikiModule);
    useEffect(() => {
        if (editor) {
            // Whenever the current Markdown content changes, converts it to an array
            // of Block objects and replaces the editor's content with them.
            const getBlocks = async () => {
                const blocks: Block[] = await editor.HTMLToBlocks(wikiModule?.content || "");
                editor.replaceBlocks(editor.topLevelBlocks, blocks);
            };
            getBlocks();
        }
    }, [editor, wikiModule]);


    // Renders the editor instance using a React component.
    return <BlockNoteView editor={editor} />;
};

export default Editor;
