import {Dispatch} from "react";
import {connect} from 'react-redux';
import {bindActionCreators} from "redux";

import actions from "../../actions";
import {WorkProgramActions} from "../../types";

import {rootState} from "../../../../store/reducers";
import {isCanEdit} from "../../getters";

const mapStateToProps = (state:rootState) => {
    return {
        isCanEdit: isCanEdit(state),
    };
};

const mapDispatchToProps = (dispatch: Dispatch<WorkProgramActions>) => ({
    // @ts-ignore
    actions: bindActionCreators(actions, dispatch),
});

// @ts-ignore
export default connect(mapStateToProps, mapDispatchToProps);
