# Test Record

Note that [Enter] means pressing Enter without writing a value

The tests are performed in the order shown below

After testing each feature we save the samples so that the other person can continue testing their feature using the same data

Start the program without an existing samples.json file

## Feature 1: Sample Registration and Status Updates (Yasser Assi)

Initially no samples are registered

No. | Test | Input | Expected Result | Actual Result | Pass/Fail |
|-|-|-|-|-|-|
|1|View samples|Choice: 3|No samples registered|"No samples registered"|Pass |
|2|Register a sample | Choice: 1, ID: s1, Type: blood |Sample registered with Received status |"Sample registered successfully" |Pass |
|3|Register a duplicate ID | Choice: 1, ID: s1|Duplicate ID rejected|"This sample already exists" |Pass |
|4|Empty ID | Choice: 1, ID: [Enter] | Empty ID rejected|"ID cannot be empty" |Pass|
|5|Empty type |Choice: 1, ID: s2, Type: [Enter] |Empty type rejected |"Type cannot be empty"|Pass |
|6|Skip Processing status |Choice: 2, ID: s1, Status: C |Status change rejected |"Invalid changing of status. Status order is R, P, C" |Pass |
|7|Change status to Processing |Choice: 2, ID: s1, Status: P |Status changed to Processing |"Status changed to Processing" |Pass |
|8|Change to current status |Choice: 2, ID: s1, Status: P |Status remains Processing |"Sample is already 'Processing'" |Pass |
|9|Unknown sample ID |Choice: 2, ID: s99 |Sample not found |"Sample not found"|Pass |
|10|Invalid status input |Choice: 2, ID: s1, Status: L |Invalid status rejected |"Invalid status. Enter P or C" |Pass |
|11|View registered samples |Choice: 3 |Only s1 is displayed |"ID: s1, Type: blood, Status: Processing, Readings: []" |Pass |

## Feature 2: Readings and Statistics (Melissa Mourad)

No. | Test | Input | Expected Result | Actual Result | Pass/Fail |
|-|-|-|-|-|-|
| | | | | | |

## Feature 3: Out-of-Range Readings (Melissa Mourad)

No. | Test | Input | Expected Result | Actual Result | Pass/Fail |
|-|-|-|-|-|-|
| | | | | | |

## Feature 4: Longest Consecutive Run and Sample Filtering (Yasser Assi)

No. | Test | Input | Expected Result | Actual Result | Pass/Fail |
|-|-|-|-|-|-|
| | | | | | |

## Save and Load

### Save (Melissa Mourad)

No. | Test | Input | Expected Result | Actual Result | Pass/Fail |
|-|-|-|-|-|-|
| | | | | | |

### Load (Yasser Assi)

No. | Test | Input | Expected Result | Actual Result | Pass/Fail |
|-|-|-|-|-|-|
| | | | | | |