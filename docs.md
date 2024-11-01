### 📚 Docs

This documentation serves as a guide for developers and users to understand how to interact with the application. It succinctly describes the application’s operation, including access to each available route and event. Modules are represented with '🧩', detailing their access points, with input (user) indicated by '📥' and output (server) by '📤', with real examples.

### 🧩 Capture

Responsible for processing and handling screenshots.

##### <img src="https://img.shields.io/badge/WS-D35400?style=flat-square" alt="WS" height="24px"> <img src="https://img.shields.io/badge/print__screen-F9E8D9?style=flat-square" alt="print_screen" height="24px">

WebSocket event that receives and stores a screenshot sent encoded in base64.

- **📥 Input**: _base64 encoded screenshot data_

  ```text
  "/9j/4AAQSkZJRgABA..."
  ```

- **📤 Output**: _confirmation message indicating the save status_

  ```text
  "The capture was saved with identifier 1"
  ```

##### <img src="https://img.shields.io/badge/GET-61AFFE?style=flat-square" alt="GET" height="24px"> <img src="https://img.shields.io/badge//capture/all-EBF3FB?style=flat-square" alt="/capture/all" height="24px">

Route that lists all registered captures in JSON format.

- **📤 Output**: _list of all captures with their details_

  ```json
  [
    {
      "id": 1,
      "file_name": "aae82232-0c87-43ad-982c-bf914bfce508.png",
      "created_at": "Mon, 14 Oct 2024 13:00:08 GMT"
    },
    {
      "id": 2,
      "file_name": "9694a72f-e80d-4ca1-a8fd-66d1e9faeba7.png",
      "created_at": "Mon, 14 Oct 2024 13:06:37 GMT"
    },
    {
      "id": 3,
      "file_name": "2d5fc293-bfe0-44e4-b5c4-2a920ecda309.png",
      "created_at": "Mon, 14 Oct 2024 13:06:37 GMT"
    }
  ]
  ```

##### <img src="https://img.shields.io/badge/GET-61AFFE?style=flat-square" alt="GET" height="24px"> <img src="https://img.shields.io/badge//capture/file/%3Cint:id%3E-EBF3FB?style=flat-square" alt="/capture/file/<int:id>" height="24px">

Route that sends the file corresponding to the capture with the specified **`id`**.

- **📤 Output**: _the capture file stored in PNG format as an attachment_

### 🧩 Error

Centralizes exception handling, providing standardized responses to the user in message format for exceptions originating from WebSocket events and in JSON format for HTTP requests. The unique error cases handled are **Not Found (404)** and **Internal Server Error (500)**. Other cases are treated as generic.

- **📤 WebSocket Output**: _simple message with description_

  ```text
  Resource not found.
  ```

- **📤 HTTP Output**: _JSON with description, named as "message"_

  ```json
  { "message": "Internal server error." }
  ```
