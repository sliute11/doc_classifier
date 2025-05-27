# 1. Delete any old models folder
$localModels = ".\models"
if (Test-Path $localModels) {
    Remove-Item $localModels -Recurse -Force
}

# 2. Copy from OneDrive
Copy-Item "C:\Users\sliute\OneDrive - ENDAVA\doc_classifier_extra\models" $localModels -Recurse

# 3. Build the image
nerdctl build -t doc-classifier:latest .

# 4. Delete models folder (optional cleanup)
Remove-Item $localModels -Recurse -Force
