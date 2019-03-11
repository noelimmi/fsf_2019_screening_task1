import React, { Component } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { addTask } from "../../actions/tasks";

class Form extends Component {
  state = {
    title: "",
    desc: "",
    assignee: "",
    status: "",
  };

  static propTypes = {
    addTask: PropTypes.func.isRequired,
  };

  onChange = e =>
    this.setState({
      [e.target.name]: e.target.value,
    });
  onSubmit = e => {
    e.preventDefault();
    const { title, desc, assignee, status } = this.state;
    const task = { title, desc, assignee, status };
    console.log(task);
    this.props.addTask(task);
  };

  render() {
    const { title, desc, assignee, status } = this.state;
    return (
      <div className="card card-body mt-4 mb-4">
        <h2>Add Task</h2>
        <form onSubmit={this.onSubmit}>
          <div className="form-group">
            <label>Title</label>
            <input
              className="form-control"
              type="text"
              name="title"
              onChange={this.onChange}
              value={title}
            />
          </div>
          <div className="form-group">
            <label>Description</label>
            <textarea
              className="form-control"
              type="text"
              name="desc"
              onChange={this.onChange}
              value={desc}
            />
          </div>
          <div className="form-group">
            <label>Assignee</label>
            <input
              className="form-control"
              type="text"
              name="assignee"
              onChange={this.onChange}
              value={assignee}
            />
          </div>
          <div className="form-group">
            <label>Status</label>
            <input
              className="form-control"
              type="text"
              name="status"
              onChange={this.onChange}
              value={status}
            />
          </div>
          <div className="form-group">
            <button type="submit" className="btn btn-primary">
              Submit
            </button>
          </div>
        </form>
      </div>
    );
  }
}

export default connect(
  null,
  { addTask },
)(Form);
