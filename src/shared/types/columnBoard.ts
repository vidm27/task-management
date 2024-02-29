import type {TaskBoard} from '@/shared/types/taskBoard'

export interface ColumnBoard{
    id: string;
    title: string;
    tasks?: TaskBoard[]
}