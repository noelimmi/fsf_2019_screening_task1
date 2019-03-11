import axios from "axios";

import { GET_TASKS, DELETE_TASK, ADD_TASK } from "./types";
import { createMessage, returnErrors } from "./messages";

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
    .catch(err =>
      dispatch(returnErrors(err.response.data, err.response.status)),
    );
};

// DELETE TASK

export const deleteTask = id => dispatch => {
  axios
    .delete(`/api/tasks/${id}/`)
    .then(res => {
      dispatch(createMessage({ deleteTask: "Task Deleted" }));
      dispatch({
        type: DELETE_TASK,
        payload: id,
      });
    })
    .catch(err => console.log(err));
};

// ADD TASK

export const addTask = task => dispatch => {
  axios
    .post("/api/tasks/", task)
    .then(res => {
      dispatch(createMessage({ taskAdded: "Task Added" }));
      dispatch({
        type: ADD_TASK,
        payload: res.data,
      });
    })
    .catch(err =>
      dispatch(returnErrors(err.response.data, err.response.status)),
    );
};
