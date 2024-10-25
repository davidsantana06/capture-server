### 📚 Docs

This documentation serves as a guide for developers and users to understand how to interact with the application. It succinctly describes the application’s operation, including access to each available route and event. Modules are represented with "🧩," detailing their access points, with input (user) indicated by "📥" and output (server) by "📤," both accompanied by real examples.

### 🧩 Capture

Responsible for processing and handling screenshots.

#### `WS` `print_screen`

![CREATE](https://img.shields.io/badge/CREATE-4CAF50?style=flat-square)

WebSocket event that receives and stores a screenshot sent encoded in base64.

- **📥 Input**: _base64 encoded screenshot data._

  ```text
  "/9j/4AAQSkZJRgABA..."
  ```

- **📤 Output**: _confirmation message indicating the save status._

  ```text
  "The capture was saved with identifier 1"
  ```

#### `GET` `/capture/all`

![READ](https://img.shields.io/badge/READ-2196F3?style=flat-square)

Route that lists all registered captures in JSON format.

- **📤 Output**: _list of all captures with their details._

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

#### `GET` `/capture/file/<int:id>`

![READ](https://img.shields.io/badge/READ-2196F3?style=flat-square)

Route that sends the file corresponding to the capture with the specified **`id`**.

- **📤 Output**: _the capture file stored in PNG format as an attachment._

### 🧩 Error

Centralizes exception handling, providing standardized responses to the user in message format for exceptions originating from WebSocket events and in JSON format for HTTP requests. The unique error cases handled are **Not Found (404)** and **Internal Server Error (500)**. Other cases are treated as generic.

- **📤 WebSocket Output**: _simple message with description._

  ```text
  Resource not found.
  ```

- **📤 HTTP Output**: _JSON with description, named as "message"._

  ```json
  { "message": "Internal server error." }
  ```
