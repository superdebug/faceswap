#!/usr/bin/env python3
""" Default configurations for extract """

import logging

from lib.config import FaceswapConfig

logger = logging.getLogger(__name__)  # pylint: disable=invalid-name


class Config(FaceswapConfig):
    """ Config File for Models """

    def set_defaults(self):
        """ Set the default values for config """
        logger.debug("Setting defaults")

        # << MTCNN DETECTOR OPTIONS >> #
        section = "detect.mtcnn"
        self.add_section(title=section,
                         info="MTCNN Detector options")
        self.add_item(
            section=section, title="minsize", datatype=int, default=20,
            info="The minimum size of a face (in pixels) to be accepted as a positive match.\n"
                 "Lower values use significantly more VRAM and will detect more false positives")
        self.add_item(
            section=section, title="threshold_1", datatype=float, default=0.6,
            info="First stage threshold for face detection. This stage obtains face candidates\n"
                 "Choose: A decimal number between 0 and 1")
        self.add_item(
            section=section, title="threshold_2", datatype=float, default=0.7,
            info="Second stage threshold for face detection. This stage refines face candidates\n"
                 "Choose: A decimal number between 0 and 1")
        self.add_item(
            section=section, title="threshold_3", datatype=float, default=0.7,
            info="Third stage threshold for face detection. This stage further refines face "
                 "candidates\nChoose: A decimal number between 0 and 1")
        self.add_item(
            section=section, title="scalefactor", datatype=float, default=0.709,
            info="The scale factor for the image pyramid\n"
                 "Choose: A decimal number between 0 and 1")
