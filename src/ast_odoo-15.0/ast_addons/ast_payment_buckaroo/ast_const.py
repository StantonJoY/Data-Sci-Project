Module(
    body=[
        Assign(
            targets=[Name(id='STATUS_CODES_MAPPING', ctx=Store())],
            value=Dict(
                keys=[
                    Constant(value='pending', kind=None),
                    Constant(value='done', kind=None),
                    Constant(value='cancel', kind=None),
                    Constant(value='refused', kind=None),
                    Constant(value='error', kind=None),
                ],
                values=[
                    Tuple(
                        elts=[
                            Constant(value=790, kind=None),
                            Constant(value=791, kind=None),
                            Constant(value=792, kind=None),
                            Constant(value=793, kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[Constant(value=190, kind=None)],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value=890, kind=None),
                            Constant(value=891, kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[Constant(value=690, kind=None)],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value=490, kind=None),
                            Constant(value=491, kind=None),
                            Constant(value=492, kind=None),
                        ],
                        ctx=Load(),
                    ),
                ],
            ),
            type_comment=None,
        ),
    ],
    type_ignores=[],
)
