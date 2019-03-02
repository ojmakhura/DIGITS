# Copyright (c) 2014-2017, NVIDIA CORPORATION.  All rights reserved.


from flask_wtf import Form
from wtforms.validators import DataRequired

from digits import utils


class DatasetForm(Form):
    """
    Defines the form used to create a new Dataset
    (abstract class)
    """

    dataset_name = utils.forms.StringField('Dataset Name',
                                           validators=[DataRequired()]
                                           )

    group_name = utils.forms.StringField('Group Name',
                                         tooltip="An optional group name for organization on the main page."
                                         )
