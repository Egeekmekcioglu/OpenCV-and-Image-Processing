{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b314c9ee-c1d4-4662-92aa-930e9072f69d",
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2\n",
    "\n",
    "img = cv2.imread('C:/Users/xboys/Downloads/Image/DATA/00-puppy.jpg')\n",
    "\n",
    "while True:\n",
    "    \n",
    "    cv2.imshow('Puppy',img)\n",
    "    \n",
    "    #IF we've waited at least 1 ms AND we've pressed the ESC\n",
    "    if cv2.waitKey(1) & 0xFF == 27:\n",
    "        break\n",
    "        \n",
    "cv2.destroyAllWindows()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
