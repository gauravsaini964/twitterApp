const initialState = {
  status: "Connected",
};

const authReducer = (state = initialState, action) => {
  switch (action.type) {
    case "SAMPLE_TYPE":
      return {
        ...state,
      };

    default:
      return state;
  }
};

export default authReducer;
