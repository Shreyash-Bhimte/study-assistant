import { useReducer } from "react";
import { uploadFile } from "../lib/api";

const initialState = {
  documentText: null,
  charCount: 0,
  messages: [],
  isLoading: false,
  error: null,
};

function reducer(state, action) {
  switch (action.type) {
    case "UPLOAD_START":
      return { ...state, isLoading: true, error: null };
    case "UPLOAD_SUCCESS":
      return {
        ...state,
        isLoading: false,
        documentText: action.text,
        charCount: action.charCount,
      };
    case "UPLOAD_ERROR":
      return { ...state, isLoading: false, error: action.error };
    case "CLEAR":
      return initialState;
    default:
      return state;
  }
}

export function useStudySession() {
  const [state, dispatch] = useReducer(reducer, initialState);

  async function handleUpload(file) {
    dispatch({ type: "UPLOAD_START" });
    try {
      const data = await uploadFile(file);
      dispatch({ type: "UPLOAD_SUCCESS", text: data.text, charCount: data.char_count });
    } catch (err) {
      dispatch({ type: "UPLOAD_ERROR", error: err.message });
    }
  }

  function clearSession() {
    dispatch({ type: "CLEAR" });
  }

  return { state, handleUpload, clearSession };
}