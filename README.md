<b> This project contains documentation and data related to the cow lameness assessment project phase 3. <b>

Directory Structure
The project's data is organized into several key directories:

.
├── raw_videos/
│   ├── long_videos_by_date/
│   ├── short_videos_by_date/
│   ├── lameness_videos_passing_orders.csv
│   └── cow_order.docx
├── short_videos_by_cow/
│   └── [cow_id]/
│       ├── good/
│       │   ├── duplicated_passing/
│       │   │   └── ... (duplicated good videos)
│       │   └── ... (good videos)
│       ├── bad/
│       │   ├── approach/
│       │   │   └── ...
│       │   ├── direction/
│       │   │   └── ...
│       │   ├── human/
│       │   │   └── ...
│       │   ├── run/
│       │   │   └── ...
│       │   ├── slip/
│       │   │   └── ...
│       │   ├── stop/
│       │   │   └── ...
│       │   └── two/
│       │       └── ...
│       └── [cow_id].jpg
├── count_video_number/
│   ├── analyze_videos.py
│   └── video_stats.json
├── meeting_notes/
│   └── ... (meeting documentation and notes)
├── plan/
│   ├── DSI_proposal_submitted.docx
│   └── gantt_chart_and_time_commitment.xlsx
└── ... (other project files)

<b> Directory Descriptions <b> 
raw_videos/: Contains the original video recordings and documentation

long_videos_by_date/: Raw video that were taken, those are long video recordings (8-30 minutes each) organized by date. We took videos twice for each cow, on the saturday of each week, once in the morning, once in the afternoon. Each video captures multiple cows walking by over an extended period
short_videos_by_date/: Shorter video clips (~15 seconds each) that contains only 1 cow walk by at a time, organized by date
lameness_videos_passing_orders.csv: CSV file containing the sequence and order of cow walking by in videos (converted from the .docx file below)
cow_order.docx: Word doc file containing the sequence and order of cow walking by in videos (the order was written done manually)
short_videos_by_cow/: Contains processed videos organized by individual cow ID

[cow_id]/: A folder for each individual cow, identified by its unique ID
good/: Contains high-quality, usable videos suitable for lameness analysis
duplicated_passing/: Good quality videos, but they are called "duplicated" because we already have another good video clip from the same cow on the same day (at the root of the good folder). We do not need to assess lameness twice for the same cow on the same day.
bad/: Contains videos unsuitable for analysis, categorized by specific quality issues
[cow_id].jpg: A representative image for each cow
count_video_number/: Contains analysis tools and results

analyze_videos.py: Python script that processes the video directory structure and generates statistics
video_stats.json: JSON output containing aggregated video counts and statistics for each cow
meeting_notes/: Contains project meeting documentation, discussions, and progress notes

plan/: Contains project planning and proposal documents

DSI_proposal_submitted.docx: Submitted project proposal document (awarded by DSI)
gantt_chart_and_time_commitment.xlsx: Project timeline and resource allocation planning
Video Analysis and Categorization
Analysis Script
The analyze_videos.py script walks through the short_videos_by_cow/ directory structure, counts videos in each category (good/bad and their subcategories), and generates comprehensive statistics saved to video_stats.json. The output includes: - Total counts of cows in the dataset - Total counts of good and bad videos - Detailed breakdown for each individual cow - Category-specific statistics

Video Quality Categories
Good Videos
good/: High-quality, usable videos where the cow's gait and behavior are clearly visible and suitable for lameness analysis
duplicated_passing/: Also considered good quality videos, specifically used to mark instances where multiple good videos exist for the same cow on the same day
Bad Videos
Videos in the bad/ category are not suitable for lameness analysis due to various quality issues. They are organized into specific subcategories based on the reason for rejection:

approach/: The cow approached too close to the camera while walking, affecting the analysis perspective
direction/: The cow is moving in the wrong direction (right to left instead of the preferred left to right movement)
human/: Excessive human interference with the cow, or humans blocking the view of the cow in the video
run/: The cow is running through the scene, making gait assessment difficult (Note: A running cow may indicate good health)
slip/: The cow slipped at some point during the video recording (subtle)
stop/: The cow stopped for a while during the video recording
two/: Multiple cows (two or more) are present in the video, making individual gait analysis difficult
