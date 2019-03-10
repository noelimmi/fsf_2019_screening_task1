import axios from "axios";

import { GET_TASKS, DELETE_TASK } from "./types";

// GET TASKS

export const getTasks = () => dispatch => {
  axios
    .get("/api/tasks/")
    .then(res => {
      dispatch({
        type: GET_TASKS,
        payload: res.data,
      });
    })
    .catch(err => console.log(err));
};

// DELETE TASK

export const deleteTask = id => dispatch => {
  axios
    .delete(`/api/tasks/${id}/`)
    .then(res => {
      dispatch({
        type: DELETE_TASK,
        payload: id,
      });
    })
    .catch(err => console.log(err));
};
