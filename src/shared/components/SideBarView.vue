<script setup lang="ts">
import BoardIcon from '@/shared/icons/BoardIcon.vue';
import LogoLight from '@/shared/icons/LogoLight.vue';

import { useBoardStore } from '@/shared/stores/board_store';

const store = useBoardStore();

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
                        <span class="ms-3">Dashboard</span>
                    </a>
                </li>
            </ul>
            <button type="button" class="flex items-center py-2 ml-7 group gap-3" v-on:click="store.addBoard('name', 'aksas')">
                <BoardIcon></BoardIcon>
                <span class="text-[#635FC7]">Create New Board</span>
            </button>
        </div>
    </aside>
</template>


<style scoped></style>
