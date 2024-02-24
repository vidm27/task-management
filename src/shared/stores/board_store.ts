import { defineStore } from "pinia";
import { computed, ref } from "vue";

interface Board{
    id: string,
    nameBoard: string,
    boardColumn?: string[]
}

export const useBoardStore = defineStore('board', () =>{
    const boards = ref<Board[]>([])
    const totalBoards = computed(() => boards.value.length)

    function addBoard(nameBoard: string, id:string, columns: string[]){
        boards.value.push({id: id, nameBoard: nameBoard, boardColumn: columns})
    }

    function addColumnBoard(id:string, nameColumns: string[]){
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