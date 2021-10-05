# Electronics Brands
DELL = 'Dell'
HP = 'HP'
LENOVO = 'Lenovo'
ACER = 'Acer'
ASUS = 'Asus'

BRAND_CHOICES = [
    (DELL, 'Dell'),
    (HP, 'HP'),
    (LENOVO, 'Lenovo'),
    (ACER, 'Acer'),
    (ASUS, 'Asus'),
]

# Devides status
NEW = 'New'
REFURBISHED = 'Refurbished'
USED = 'Used'

DEVICE_STATUS_CHOICES = [
    (NEW, 'New'),
    (REFURBISHED, 'Refurbished'),
    (USED, 'Used'),
]

# Processor Types
INTEL_I3 = 'intel i3'
INTEL_I5 = 'intel i5'
INTEL_I7 = 'intel i7'
DUAL_CORE = 'Dual Core'

PROCESSOR_TYPE_CHOICES = [
    (INTEL_I3, 'intel i3'),
    (INTEL_I5, 'intel i5'),
    (INTEL_I7, 'intel i7'),
    (DUAL_CORE, 'Dual Core'),
]

# RAM Types
DRAM = 'DRAM'
SRAM = 'SRAM'

RAM_TYPE_CHOICES = [
    (DRAM, 'DRAM'),
    (SRAM, 'SRAM'),
]

# RAM Sizes
FIVE12 = '512MB'
ONE_GB = '1GB'
TWO_GB = '2GB'
FOUR_GB = '4GB'
EGIHT_GB = '8GB'

RAM_SIZE_CHOICES = [
    (FIVE12, '512MB'),
    (ONE_GB, '1GB'),
    (TWO_GB, '2GB'),
    (FOUR_GB, '4GB'),
    (EGIHT_GB, '8GB'),
]

# Storage Types
SSD = 'SDD'
HDD = 'HDD'
ROM = 'ROM'
SD_CARD = 'SD Card'

STORAGE_TYPE_CHOICES = [
    (SSD, 'SSD'),
    (HDD, 'HDD'),
    (ROM, 'ROM'),
    (SD_CARD, 'SD Card'),
]

# Storage Sizes

GB80 = '80GB'
GB128 = '128GB'
GB160 = '160GB'
GB250 = '250GB'
GB320 = '320GB'
GB500 = '500GB'
TB1 = '1TB'

STORAGE_SIZE_CHOICES = [
    (GB80, '80GB'),
    (GB128, '128GB'),
    (GB160, '160GB'),
    (GB250, '250GB'),
    (GB320, '320GB'),
    (GB500, '500GB'),
    (TB1, '1TB'),
]

# OS Type Installed
MAC = 'Mac OS'
WINDOWS = 'Windows'
LINUX = 'Linux'

OS_TYPE_CHOICES = [
    (MAC, 'Mac OS'),
    (WINDOWS, 'Windows'),
    (LINUX, 'Linux'),
]

# Computer Status
WORKING = 'Working'
PROBLEMATIC = 'Problematic'
DESPATCHED = 'Dispatched'
PROCESSED = 'Processed'
EWASTE = 'E-Waste'

COMPUTER_STATUS_CHOICES = [
    (WORKING, 'Working'),
    (PROBLEMATIC, 'Problematic'),
    (DESPATCHED, 'Dispatched'),
    (PROCESSED, 'Processed'),
    (EWASTE, 'E-Waste'),
]

# Device type choices
SYSTEM_UNIT = 'System Unit'
TABLET = 'Tablet'
LAPTOP = 'Laptop'
PRINTER = 'Printer'
PROJECTOR = 'Projector'

DEVICE_TYPE_CHOICES = [
    (SYSTEM_UNIT, 'System Unit'),
    (TABLET, 'Tablet'),
    (LAPTOP, 'Laptop'),
    (PRINTER, 'Printer'),
    (PROJECTOR, 'Projector'),
]