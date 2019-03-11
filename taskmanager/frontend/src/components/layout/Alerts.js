import React, { Component, Fragment } from "react";
import { withAlert } from "react-alert";
import { connect } from "react-redux";
import PropTypes from "prop-types";

export class Alerts extends Component {
  static propTypes = {
    error: PropTypes.object.isRequired,
    message: PropTypes.object.isRequired,
  };
  componentDidUpdate(prevProps) {
    const { error, alert, message } = this.props;
    if (error !== prevProps.error) {
      if (error.msg.title) alert.error(`Title:${error.msg.title.join()}`);
      if (error.msg.desc) alert.error(`Description:${error.msg.desc.join()}`);
      if (error.msg.assignee)
        alert.error(`Assignee:${error.msg.assignee.join()}`);
      if (error.msg.status) alert.error(`Status:${error.msg.status.join()}`);
    }

    if (message !== prevProps.message) {
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
