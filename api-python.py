import cv2

def evaluate_image_quality(image_path):
    # Đọc hình ảnh
    img = cv2.imread(image_path)

    # Tính toán độ tương phản (Contrast)
    contrast = cv2.mean(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))[0]

    # Tính toán độ sáng (Brightness)
    brightness = cv2.mean(img)[0]

    # Tính toán mức độ nhiễu (Noise) trong hình ảnh
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    noise = cv2.Laplacian(gray_img, cv2.CV_64F).var()

    return contrast, brightness, noise

# Gọi hàm để lấy các thông số của hình ảnh
image_path = 'path/to/your/image.jpg'
contrast, brightness, noise = evaluate_image_quality(image_path)

print(f"Độ tương phản: {contrast}")
print(f"Độ sáng: {brightness}")
print(f"Mức độ nhiễu: {noise}")




import cv2

def calculate_contrast(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    contrast = cv2.meanStdDev(img)[1][0][0]
    return contrast

def calculate_brightness(image_path):
    img = cv2.imread(image_path)
    brightness = cv2.mean(img)[0]
    return brightness

def calculate_sharpness(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    laplacian_var = cv2.Laplacian(img, cv2.CV_64F).var()
    return laplacian_var

def calculate_noise(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    noise = cv2.meanStdDev(img)[1][0][0]
    return noise

def calculate_image_size(image_path):
    img = cv2.imread(image_path)
    height, width = img.shape[:2]
    return width, height

def calculate_aspect_ratio(image_path):
    img = cv2.imread(image_path)
    height, width = img.shape[:2]
    aspect_ratio = width / height
    return aspect_ratio

# Đường dẫn đến hình ảnh
image_path = 'path/to/your/image.jpg'

# Tính các thông số liên quan đến chất lượng hình ảnh
contrast = calculate_contrast(image_path)
brightness = calculate_brightness(image_path)
sharpness = calculate_sharpness(image_path)
noise = calculate_noise(image_path)
width, height = calculate_image_size(image_path)
aspect_ratio = calculate_aspect_ratio(image_path)

# In kết quả
print(f"Độ tương phản: {contrast}")
print(f"Độ sáng: {brightness}")
print(f"Độ sắc nét: {sharpness}")
print(f"Mức độ nhiễu: {noise}")
print(f"Kích thước ảnh (Width x Height): {width} x {height}")
print(f"Tỷ lệ khung hình (Aspect ratio): {aspect_ratio}")
