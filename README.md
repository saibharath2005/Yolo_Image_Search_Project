# YOLOv11 Search Application

This project is a Computer Vision powered image search system built using **YOLOv11** for object detection and **Streamlit** for the web user interface. It allows users to process images, extract object metadata, and search images based on classes and object counts.

---

## 🔥 Key Features

* Run object detection using YOLOv11 on a folder of images.
* Automatically save detection results as structured metadata.
* Load previously processed metadata without re-running inference.
* Search images by:

  * Classes (objects) present
  * Object count thresholds
  * Match mode (ANY / ALL selected classes)
* View results in a responsive image grid.
* Highlight matching objects in the results.
* Export search results as JSON.

---

## 🗂️ Project Workflow

1. **Choose images to process** → Run YOLO inference.
2. **Metadata is saved** in `processed/<dataset>/metadata.json`.
3. You can **load metadata** later without processing again.
4. User selects classes and count filters.
5. Matching images are shown with bounding boxes and labels.

---

## 🧠 Search Modes Explained

| Mode          | Meaning                                                      |
| ------------- | ------------------------------------------------------------ |
| **Any (OR)**  | Image is shown if it contains *at least one* selected class. |
| **All (AND)** | Image is shown only if it contains *all* selected classes.   |

You can also apply **count limits**, e.g.,

* "Show images with *spoon* count ≤ 2"
* "Show images with exactly *1 banana*"

---

## 📦 Tech Stack

| Component        | Technology            |
| ---------------- | --------------------- |
| Object Detection | **YOLOv11** (PyTorch) |
| UI Frontend      | **Streamlit**         |
| Image Rendering  | **Pillow (PIL)**      |
| Data Storage     | JSON Metadata         |

---

## 🚀 Running the Application

1. Install requirements:

```
pip install -r requirements.txt
```

2. Run Streamlit app:

```
streamlit run app.py
```

3. Upload or specify image folder path and model weights.

---

## 📂 Metadata Format Example

Each processed image produces metadata like:

```
{
  "image_path": "path/to/img.jpg",
  "detections": [
    {"class": "banana", "confidence": 0.85, "bbox": [...], "count": 1 },
    ...
  ],
  "class_counts": {
      "banana": 1,
      "bowl": 2
  }
}
```

---

## ✅ Result Display

* Bounding boxes drawn on objects.
* Matching classes highlighted in green.
* Non-matching objects shown faded (optional).

---

## 📤 Export Search Results

You can download:

* Filtered results as `search_results.json`

---


## Real-World Use Cases

This project can be applied in various domains where large collections of images need to be searched based on objects present within them:

| Domain / Field                | Usage                                                                                                   |
| ----------------------------- | ------------------------------------------------------------------------------------------------------- |
| **Surveillance / Security**   | Search CCTV images for persons, vehicles, or suspicious items. Useful in investigations and monitoring. |
| **Retail / Store Analytics**  | Analyze crowd presence or product shelf states using image data. Helps in planning & customer analysis. |
| **Traffic Monitoring**        | Detect and count cars, bikes, and pedestrians from street images. Useful for smart city systems.        |
| **Wildlife Monitoring**       | Identify animals from forest camera trap images. Helps researchers track species.                       |
| **Medical Imaging Research**  | Organize and filter medical images based on detected features (e.g., cells, abnormalities).             |
| **Photo Library Management**  | Search personal or event photos containing people, pets, or groups.                                     |
| **Forensics & Investigation** | Quickly filter crime scene images containing specific objects (e.g., weapons, vehicles).                |

This makes the system **highly useful** wherever image datasets are large and manual searching is **time-consuming or impossible**.


