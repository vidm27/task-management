import type { ColumnBoard } from "./columnBoard";

export interface Board{
    id: string,
    nameBoard: string,
    boardColumn?: ColumnBoard[]
}