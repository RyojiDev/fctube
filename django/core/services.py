class VideoService:

    def process_upload(self, video_id: int, chunk_index: int, chunk:bytes):
        print(f'Processing upload for video {video_id}, chunck {chunk_index}')

    def finalize_upload(self, video_id: int, total_chunks: int, ):
        print(f'Finalizing upload for video {video_id}')