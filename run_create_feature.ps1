$featureDescription = Get-Content -Path 'temp_feature_spec.md' -Raw
.specify/scripts/powershell/create-new-feature.ps1 -Number 1 -ShortName 'book-rag-chatbot' -Json $featureDescription