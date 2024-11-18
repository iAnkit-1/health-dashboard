import React, { useState } from "react";
import "./Dashboard.css"; // Importing the CSS file

const Dashboard = () => {
  const [formData, setFormData] = useState({
    name: "",
    age: "",
    file: null,
  });

  const handleChange = (e) => {
    const { name, value, files } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: files ? files[0] : value,
    }));
  };

  const handleSubmit = () => {
    console.log(formData);
    alert("Form submitted!");
  };

  return (
    <div className="dashboard-container">
      <h1 className="dashboard-title">Healthcare Dashboard</h1>
      <form className="dashboard-form">
        <label className="form-label">Name</label>
        <input
          type="text"
          name="name"
          className="form-input"
          onChange={handleChange}
        />

        <label className="form-label">Age</label>
        <select
          name="age"
          className="form-input"
          onChange={handleChange}
        >
          <option value="">Select Age</option>
          {[...Array(100).keys()].map((i) => (
            <option key={i} value={i + 1}>
              {i + 1}
            </option>
          ))}
        </select>

        <label className="form-label">File Upload</label>
        <input
          type="file"
          name="file"
          className="form-input"
          onChange={handleChange}
        />

        <button
          type="button"
          className="form-button"
          onClick={handleSubmit}
        >
          Submit
        </button>
      </form>
    </div>
  );
};

export default Dashboard;
