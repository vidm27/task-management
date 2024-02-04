import { defineStore } from "pinia";
import { computed, ref } from "vue";

interface Board{
    id: string,
    nameBoard: string,
    boardColumn?: []
}

export const useBoardStore = defineStore('board', () =>{
    const boards = ref<Board[]>([])
    const totalBoards = computed(() => boards.value.length)

    function addBoard(nameBoard: string, id:string){
        boards.value.push({id: id, nameBoard: nameBoard})
    }

    return {
        boards,
        addBoard,
        totalBoards
    }
})