Module(
    body=[
        Import(
            names=[alias(name='json', asname='json_')],
        ),
        Import(
            names=[alias(name='re', asname=None)],
        ),
        Import(
            names=[alias(name='markupsafe', asname=None)],
        ),
        Assign(
            targets=[Name(id='JSON_SCRIPTSAFE_MAPPER', ctx=Store())],
            value=Dict(
                keys=[
                    Constant(value='&', kind=None),
                    Constant(value='<', kind=None),
                    Constant(value='>', kind=None),
                    Constant(value='\u2028', kind=None),
                    Constant(value='\u2029', kind=None),
                ],
                values=[
                    Constant(value='\\u0026', kind=None),
                    Constant(value='\\u003c', kind=None),
                    Constant(value='\\u003e', kind=None),
                    Constant(value='\\u2028', kind=None),
                    Constant(value='\\u2029', kind=None),
                ],
            ),
            type_comment=None,
        ),
        ClassDef(
            name='_ScriptSafe',
            bases=[Name(id='str', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='__html__',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='markupsafe', ctx=Load()),
                                    attr='Markup',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='re', ctx=Load()),
                                            attr='sub',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='[<>&\\u2028\\u2029]', kind=None),
                                            Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(arg='m', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=Subscript(
                                                    value=Name(id='JSON_SCRIPTSAFE_MAPPER', ctx=Load()),
                                                    slice=Subscript(
                                                        value=Name(id='m', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    ctx=Load(),
                                                ),
                                            ),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='JSON',
            bases=[],
            keywords=[],
            body=[
                FunctionDef(
                    name='loads',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=arg(arg='args', annotation=None, type_comment=None),
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='json_', ctx=Load()),
                                    attr='loads',
                                    ctx=Load(),
                                ),
                                args=[
                                    Starred(
                                        value=Name(id='args', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=Name(id='kwargs', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='dumps',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=arg(arg='args', annotation=None, type_comment=None),
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' JSON used as JS in HTML (script tags) is problematic: <script>\n        tags are a special context which only waits for </script> but doesn\'t\n        interpret anything else, this means standard htmlescaping does not\n        work (it breaks double quotes, and e.g. `<` will become `&lt;` *in\n        the resulting JSON/JS* not just inside the page).\n\n        However, failing to escape embedded json means the json strings could\n        contains `</script>` and thus become XSS vector.\n\n        The solution turns out to be very simple: use JSON-level unicode\n        escapes for HTML-unsafe characters (e.g. "<" -> "<". This removes\n        the XSS issue without breaking the json, and there is no difference to\n        the end result once it\'s been parsed back from JSON. So it will work\n        properly even for HTML attributes or raw text.\n\n        Also handle U+2028 and U+2029 the same way just in case as these are\n        interpreted as newlines in javascript but not in JSON, which could\n        lead to oddities and issues.\n\n        .. warning::\n\n            except inside <script> elements, this should be escaped following\n            the normal rules of the containing format\n\n        Cf https://code.djangoproject.com/ticket/17419#comment:27\n        ', kind=None),
                        ),
                        Return(
                            value=Call(
                                func=Name(id='_ScriptSafe', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='json_', ctx=Load()),
                                            attr='dumps',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Starred(
                                                value=Name(id='args', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg=None,
                                                value=Name(id='kwargs', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        Assign(
            targets=[Name(id='scriptsafe', ctx=Store())],
            value=Call(
                func=Name(id='JSON', ctx=Load()),
                args=[],
                keywords=[],
            ),
            type_comment=None,
        ),
    ],
    type_ignores=[],
)
