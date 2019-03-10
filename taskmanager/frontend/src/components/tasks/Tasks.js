import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import propTypes from "prop-types";
import { getTasks, deleteTask } from "../../actions/tasks";

export class Tasks extends Component {
  static propTypes = {
    tasks: propTypes.array.isRequired,
    getTasks: propTypes.func.isRequired,
    deleteTask: propTypes.func.isRequired,
  };
  componentDidMount() {
    this.props.getTasks();
  }
  render() {
    return (
      <Fragment>
        <h2>Tasks</h2>
        <table className="table table-striped">
          <thead>
            <tr>
              <th>ID</th>
              <th>Title</th>
              <th>Description</th>
              <th>Assignee</th>
              <th>Status</th>
              <th>Created</th>
              <th />
            </tr>
          </thead>
          <tbody>
            {this.props.tasks.map(task => (
              <tr key={task.id}>
                <td>{task.id}</td>
                <td>{task.title}</td>
                <td>{task.desc}</td>
                <td>{task.assignee}</td>
                <td>{task.status}</td>
                <td>{task.created_at}</td>
                <td>
                  <button
                    onClick={this.props.deleteTask.bind(this, task.id)}
                    className="btn btn-danger btn-sm"
                  >
                    Delete
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </Fragment>
    );
  }
}

//to map application state to props of this component
const mapStateToProps = state => ({
  //anything: state.tasksreducer. part of state ie tasks
  tasks: state.tasks.tasks,
});

export default connect(
  mapStateToProps,
  { getTasks, deleteTask },
)(Tasks);
