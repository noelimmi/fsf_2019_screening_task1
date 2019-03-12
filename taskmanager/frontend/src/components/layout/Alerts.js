import React, { Component, Fragment } from "react";
import { withAlert } from "react-alert";
import { connect } from "react-redux";
import propTypes from "prop-types";

export class Alerts extends Component {
  static propTypes = {
    error: propTypes.object.isRequired,
    message: propTypes.object.isRequired,
  };
  componentDidUpdate(prevProps) {
    const { error, alert, message } = this.props;
    if (error !== prevProps.error) {
      if (error.msg.title) alert.error(`Title: ${error.msg.title.join()}`);
      if (error.msg.desc) alert.error(`Description: ${error.msg.desc.join()}`);
      if (error.msg.assignee)
        alert.error(`Assignee: ${error.msg.assignee.join()}`);
      if (error.msg.status) alert.error(`Status: ${error.msg.status.join()}`);
      if (error.msg.username)
        alert.error(`Username: ${error.msg.username.join()}`);
      if (error.msg.password)
        alert.error(`Password: ${error.msg.password.join()}`);
      if (error.msg.non_field_errors)
        alert.error(error.msg.non_field_errors.join());
      if (error.msg.username) alert.error(error.msg.username.join());
      if (error.msg.username) alert.error(error.msg.username.join());
    }

    if (message !== prevProps.message) {
      if (message.passwordNotMatch) alert.error(message.passwordNotMatch);
      if (message.deleteTask) alert.success(message.deleteTask);
      if (message.taskAdded) alert.success(message.taskAdded);
    }
  }
  render() {
    return <Fragment />;
  }
}

const mapStateToProps = state => ({
  error: state.errors,
  message: state.messages,
});

export default connect(mapStateToProps)(withAlert(Alerts));
