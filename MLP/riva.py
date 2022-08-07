from nemo.collections.tts.models import FastPitchModel

checkpoint = 'FastPitch_twilight_sparkle.ckpt'
spec_model = FastPitchModel.load_from_checkpoint(checkpoint)
spec_model.save_to('twilight_sparkle_FastPitch_model02.nemo')
