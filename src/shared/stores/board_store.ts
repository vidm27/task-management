import { defineStore } from "pinia";
import { computed, ref } from "vue";
import type { ColumnBoard } from "../types/columnBoard";
import type { Board } from "../types/board";



export const useBoardStore = defineStore('board', () =>{
    const boards = ref<Board[]>([])
    const totalBoards = computed(() => boards.value.length)

    function addBoard(nameBoard: string, id:string, columns: ColumnBoard[]){
        boards.value.push({id: id, nameBoard: nameBoard, boardColumn: columns})
    }

    function addColumnBoard(id:string, nameColumns: ColumnBoard[]){
        for (const board of boards.value) {
            if(board.id === id){
                for (const column of nameColumns) {
                    board.boardColumn?.push(column)
                }
            }
        }
    }

    return {
        boards,
        addBoard,
        addColumnBoard,
        totalBoards
    }
})