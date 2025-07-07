# Audio-CNN: Audio Classification with Convolutional Neural Networks

## Overview

Audio-CNN is a deep learning project for audio classification using Convolutional Neural Networks. The system is trained on the ESC-50 dataset (Environmental Sound Classification) and can classify various environmental sounds into 50 categories with high accuracy. The project includes both a backend model for training and inference, and a modern web frontend for interactive visualization.

## Features

- **Audio Classification**: Classify environmental sounds into 50 categories with confidence scores
- **Interactive Visualization**: View spectrograms, waveforms, and CNN layer activations
- **Modern UI**: Clean, responsive interface with dark/light mode support
- **Sample Audio Analysis**: Try the model with included sample audio files
- **Real-time Inference**: Fast audio processing and classification
- **Emoji Mapping**: Visual representation of sound categories with relevant emojis
- **Layer Visualization**: Explore internal CNN activations for interpretability

## Project Structure

```
├── audio-cnn-frontend/    # Next.js frontend application
├── main.py                # Modal deployment for inference
├── model.py               # CNN model architecture
├── train.py               # Training script
├── requirements.txt       # Python dependencies
└── chirpingbirds.wav      # Sample audio file
```

## Dataset

This project uses the [ESC-50 dataset](https://github.com/karolpiczak/ESC-50), which contains 2000 environmental audio recordings organized into 50 semantic classes:

- **Animals**: Dog, rooster, pig, cow, frog, cat, hen, insects, sheep, crow
- **Natural soundscapes**: Rain, sea waves, crackling fire, crickets, chirping birds, water drops, wind, thunderstorm
- **Human, non-speech sounds**: Crying baby, sneezing, clapping, breathing, coughing, footsteps, laughing, brushing teeth, snoring, drinking/sipping
- **Interior/domestic sounds**: Door knock, door/wood creaks, can opening, washing machine, vacuum cleaner, clock alarm, clock tick, glass breaking, toilet flush, toothbrush
- **Exterior/urban noises**: Helicopter, chainsaw, siren, car horn, engine, train, church bells, airplane, fireworks, hand saw

Each recording is 5 seconds long with a sampling rate of 44.1kHz.

## Model Architecture

The project uses a ResNet-inspired CNN architecture with the following components:

- Convolutional layers with residual connections
- Batch normalization and ReLU activations
- Adaptive average pooling
- Dropout (0.5) for regularization
- Fully connected layer for classification

The model processes audio by:
1. Converting raw audio to mel spectrograms (128 mel bands)
2. Applying data augmentation (frequency masking, time masking)
3. Feeding the spectrograms through the CNN
4. Outputting class probabilities via softmax

## Backend (Python/PyTorch)

### Prerequisites

- Python 3.8+
- PyTorch 2.0+
- Modal (for deployment)

### Installation

```bash
# Clone the repository
git clone https://github.com/sudipto0315/Audio-CNN.git
cd Audio-CNN

# Install dependencies
pip install -r requirements.txt
```

### Training

The model is trained on the ESC-50 dataset using Modal's cloud infrastructure:

```bash
modal run train.py
```

Training includes:
- Data augmentation with frequency and time masking
- MixUp augmentation for improved generalization
- OneCycleLR learning rate scheduling
- TensorBoard logging for monitoring progress

### Inference

Run inference on a local audio file:

```bash
modal run main.py
```

Or deploy as an API endpoint:

```bash
modal deploy main.py
```

The Modal deployment:
- Uses GPU acceleration (A10G) for faster inference
- Loads the model from a persistent volume
- Provides a FastAPI endpoint for audio processing
- Returns predictions and visualization data in JSON format

## Frontend (Next.js)

### Technologies Used

- **Next.js**: React framework with App Router
- **Tailwind CSS**: Utility-first CSS framework
- **next-themes**: Theme management with dark/light mode support
- **Radix UI**: Accessible UI components
- **TypeScript**: Type-safe JavaScript

### Architecture

The frontend follows a component-based architecture:

- **Components**:
  - `ColorScale.tsx`: Renders a color gradient scale for visualizations
  - `FeatureMap.tsx`: Renders CNN activation maps as heatmaps
  - `Waveform.tsx`: Renders audio waveform visualization
  - `theme-provider.tsx`: Provides theme context to the application
  - `theme-toggle.tsx`: Toggle button for switching between light and dark modes
  - UI components: Button, Card, Badge, Progress

- **Data Flow**:
  1. Audio file upload or sample selection
  2. Base64 encoding and API request to Modal endpoint
  3. Processing response data for visualization
  4. Rendering predictions and visualizations

### Prerequisites

- Node.js 18+
- npm or yarn

### Installation

```bash
cd audio-cnn-frontend
npm install
```

### Development

```bash
npm run dev
```

### Building for Production

```bash
npm run build
npm run start
```

## Usage

1. Start the frontend application
2. Deploy the Modal inference endpoint
3. Upload an audio file or select a sample from the provided options
4. View the classification results and visualizations

### Sample Audio Files

The application comes with several pre-loaded sample audio files for testing:

- `1-100210-B-36.wav`
- `1-172649-D-40.wav`
- `1-172649-E-40.wav`
- `1-172649-F-40.wav`
- `1-26806-A-1.wav`
- `1-30709-C-23.wav`

These files are from the ESC-50 dataset and represent different environmental sound categories.

## Visualizations

The application provides several interactive visualizations:

- **Input Spectrogram**: Mel spectrogram of the input audio with color scale
- **Audio Waveform**: Time-domain representation of the audio signal
- **Convolutional Layer Outputs**: Activation maps from different CNN layers
  - Main layer outputs
  - Internal feature maps for each layer
  - Color-coded intensity visualization

## Environment Variables

For the frontend, create a `.env.local` file with:

```
NEXT_PUBLIC_MODAL_INFERENCE_URL=https://your-modal-endpoint.modal.run
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source. Consider adding a LICENSE file to specify terms of use.

## Future Improvements

Potential enhancements for this project:

- **Model Improvements**:
  - Experiment with different CNN architectures (EfficientNet, MobileNet)
  - Implement attention mechanisms for better feature extraction
  - Add support for longer audio files and real-time streaming

- **Frontend Enhancements**:
  - Add audio recording capability directly from the browser
  - Implement more detailed visualizations (e.g., 3D feature maps)
  - Add user accounts to save and compare analysis results

- **Deployment Options**:
  - Create a containerized version with Docker
  - Add CI/CD pipeline for automated testing and deployment
  - Optimize for mobile devices

## Conclusion

Audio-CNN demonstrates the power of convolutional neural networks for audio classification tasks. By combining a robust backend model with an interactive frontend visualization, this project provides both practical utility and educational value for understanding how deep learning models process and classify audio data.

## Acknowledgments

- [ESC-50 Dataset](https://github.com/karolpiczak/ESC-50) for providing the environmental sound recordings
- [Modal](https://modal.com) for the serverless infrastructure and GPU acceleration
- [Next.js](https://nextjs.org) and [Tailwind CSS](https://tailwindcss.com) for the frontend framework
- [PyTorch](https://pytorch.org) and [torchaudio](https://pytorch.org/audio) for audio processing and deep learning capabilities