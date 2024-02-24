<script setup lang="ts">
import BoardIcon from '@/shared/icons/BoardIcon.vue';
import LogoLight from '@/shared/icons/LogoLight.vue';

import { useBoardStore } from '@/shared/stores/board_store';
import { v4 as uuidv4 } from 'uuid';
import { ref } from 'vue';

const store = useBoardStore();
interface Board {
    id: string,
    nameBoard: string,
    boardColumn?: string[]
}
const board = ref<Board>({ id: '', nameBoard: '', boardColumn: [] });

function addColumn(nameColumn: string) {
    board.value.boardColumn?.push(nameColumn);
}

</script>

<template>
    <aside id="default-sidebar"
        class="fixed top-0 left-0 z-40 w-64 h-screen transition-transform -translate-x-full sm:translate-x-0"
        aria-label="Sidebar">
        <div class="h-full pr-3 py-4 overflow-y-auto bg-gray-50 dark:bg-[#2B2C37]">
            <div class="flex items-center justify-center px-5 py-7">
                <LogoLight></LogoLight>
            </div>
            <div class="px-7 mb-3">
                <span class="uppercase text-[#828FA3] text-xs tracking-[.15em]">All Boards(0)</span>
            </div>
            <ul class="space-y-2 font-medium">
                <li v-for="board in store.boards" :key="board.id">
                    <a href="#"
                        class="flex transition ease-in-out duration-300 items-center p-2 pl-7 text-gray-900 rounded-r-[2rem] dark:text-white hover:bg-gray-100 dark:hover:bg-[#635FC7] group">
                        <BoardIcon></BoardIcon>
                        <span class="ms-3">{{ board.nameBoard }}</span>
                    </a>
                </li>
            </ul>
            <button type="button" class="flex items-center py-2 ml-7 group gap-3" onclick="new_board.showModal()">
                <BoardIcon></BoardIcon>
                <span class="text-[#635FC7]">Create New Board</span>
            </button>
            <dialog id="new_board" class="modal">
                <div class="modal-box bg-[#2B2C37]">
                    <h3 class="font-bold text-lg text-white">Add New Board</h3>
                    <label for="" class="form-control w-full mb-3">
                        <div class="label">
                            <span class="label-text">Board Name</span>
                        </div>
                        <input type="text" v-model="board.nameBoard" name="" id="" placeholder="e.g Web Design"
                            class="input input-bordered w-full bg-[#2B2C37] focus:input-primary">
                    </label>
                    <div class="form-control">
                        <div class="label">
                            <span class="label-text">Board Columns</span>
                        </div>
                        <div class="w-full">
                            <label v-for="(boardColumn, index) in board.boardColumn" :key="index" for=""
                                class="form-control w-full mb-3 flex-row gap-2">
                                <input type="text" v-model="board.boardColumn![index]" name="" id=""
                                    placeholder="name column"
                                    class="input input-bordered w-full bg-[#2B2C37] focus:input-primary text-white">
                                <div class="label">
                                    <span class="label-text"><svg width="15" height="15" xmlns="http://www.w3.org/2000/svg"
                                            v-on:click="board.boardColumn?.pop()">
                                            <g fill="#828FA3" fill-rule="evenodd">
                                                <path d="m12.728 0 2.122 2.122L2.122 14.85 0 12.728z" />
                                                <path d="M0 2.122 2.122 0 14.85 12.728l-2.122 2.122z" />
                                            </g>
                                        </svg></span>
                                </div>
                            </label>
                        </div>
                        <button type="button" class="btn bg-[#ffffff] text-[#635FC7] hover:bg-[#ffff] hover:text-[#635FC7]"
                            v-on:click="addColumn('')">
                            <svg class="fill-[#635FC7] hover:fill-[#ffff]" width="12" height="12"
                                xmlns="http://www.w3.org/2000/svg">
                                <path d="M7.368 12V7.344H12V4.632H7.368V0H4.656v4.632H0v2.712h4.656V12z" />
                            </svg>
                            <span>Add New Column</span>
                        </button>
                    </div>
                    <form method="dialog" class="modal-backdrop">
                        <button>close</button>
                        <div class="modal-action">
                            <button type="button"
                                class="btn bg-[#635FC7] text-[#ffff] hover:bg-[#635FC7] hover:text-[#ffff] w-full"
                                v-on:click="store.addBoard(board.nameBoard, uuidv4(), board.boardColumn!)">
                                <span>Create New Board</span>
                            </button>
                        </div>
                    </form>
                </div>
            </dialog>
        </div>
    </aside>
</template>


<style scoped></style>
